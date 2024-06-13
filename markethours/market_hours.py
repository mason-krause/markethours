import time
import datetime
import requests
from pytz import timezone


class MarketHours:
  '''
  A utility for accessing US trading hours

  :param str date_str: (optional- default is today) set a specific date ('%Y-%m-%d')
  '''
  def __init__(self, date_str=''):
    self.est = timezone('US/Eastern')
    self.date_str = datetime.datetime.now(self.est).strftime('%Y-%m-%d') if date_str == '' else date_str
    #: Market opening time
    self.open: datetime.datetime = None
    #: Market closing time
    self.close: datetime.datetime = None
    self.__set_market_hours()

  def __check_market_hours(self):
    r = requests.get('https://markethours.info/api', params={'date': self.date_str})
    if r.status_code in (200, 201):
      return r.json()
    
  def __set_market_hours(self):
    hours = self.__check_market_hours()
    if hours == None or hours['open'] == '00:00:00': # in case you change_date('%Y-%m-%d')
      self.open = None
      self.close = None
    else:
      self.open = self.est.localize(
        datetime.datetime.combine(
          datetime.datetime.strptime(self.date_str, '%Y-%m-%d'), 
          datetime.datetime.strptime(hours['open'], '%H:%M:%S').time()))
      self.close = self.est.localize(
        datetime.datetime.combine(
          datetime.datetime.strptime(self.date_str, '%Y-%m-%d'), 
          datetime.datetime.strptime(hours['close'], '%H:%M:%S').time()))   
      
  def change_date(self, new_date_str):
    '''
    Change to a different date

    :param str new_date_str: the new date to set ('%Y-%m-%d')
    '''
    self.date_str = new_date_str
    self.__set_market_hours()
  
  def market_has_closed(self) -> bool:
    '''Check if the market has closed'''
    if self.close == None:
      return True
    elif datetime.datetime.now(self.est) < self.close:
      return False
    else:
      return True  
        
  def market_has_opened(self) -> bool:
    '''Check if the market has opened'''
    if self.open == None:
      return False
    elif datetime.datetime.now(self.est) > self.open:
      return True
    else:
      return False
    
  def seconds_till_close(self) -> int:
    '''Calculates how many seconds until market close'''
    if self.close != None:
      now = datetime.datetime.now(self.est)
      return (self.close - now).total_seconds()
    
  def seconds_till_open(self) -> int:
    '''Calculates how many seconds until market open'''
    if self.open != None:
      now = datetime.datetime.now(self.est)
      return (self.open - now).total_seconds()

  def wait_for_market_open(self):
    '''Waits until market open'''
    if self.open == None:
      return
    now = datetime.datetime.now(self.est)
    if self.open > now:
      time.sleep((self.open - now).total_seconds())
  
  def now_est(self) -> datetime.datetime:
    '''Returns the current time in EST'''
    return datetime.datetime.now(self.est)