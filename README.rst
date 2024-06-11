``markethours``: A python library for referencing and localizing US stock trading hours
========================================================================================

``markethours`` overview
+++++++++++++++++++++++++

We created market ``markethours`` and the markethours.info API because we couldn't
find other free tools for accessing stock trading hours, and we wanted to provide
this library to help others experiencing similar issues. 

``markethours`` features include:

* Reference stock trading hours by date
* Automatically localize to Eastern Standard time
* Easily check whether market has opened or closed
* No user accounts needed


Getting started with ``markethours`` 
+++++++++++++++++++++++++++++++++++++

Installation
------------

.. code-block:: shell

  pip install markethours

Example usage
--------------

.. code-block:: python

  from markethours import MarketHours


  def main():
    todays_hours = MarketHours()

    # Check if the market has opened
    print(todays_hours.market_has_opened())

    # Check if the market has closed
    print(todays_hours.market_has_closed())

    # Wait for the market to open
    todays_hours.wait_for_market_open()

    # See the number of seconds until open
    print(todays_hours.seconds_till_open())

    # Do something if there's less than a minute before
    # close. Something like this could be used in a loop
    if todays_hours.seconds_till_close() < 60:
      print('Hurry up!')

    # Show open, close, and current time in EST
    print(todays_hours.open)
    print(todays_hours.close)
    print(todays_hours.now_est())


  if __name__ == '__main__':
    main()


**Disclaimer:** *markethours comes with no warranty of any kind, and its authors 
accept no responsibility for any damage that might stem from use of this package. 
See the LICENSE file for more details.*