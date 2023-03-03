## Coffee Machine

This program simulates a coffee vending machine through command line input.

To run the program, simply execute the `main.py` file. The commands necessary must be typed and then press enter.

Program features:
<ul>
<li>3 items in menu: espresso, latte, cappuccino;</li>
<li>Availability check on items in menu;</li>
<li>Resource management: water, milk, coffee, money;</li>
<li>Order handling: check availability, process payment, update resources;</li>
<li>Admin functions: turn off and resources report;</li>
</ul>


Making an order

![](https://i.imgur.com/XCvnFje.png)

Type the desired item in the menu as shown: espresso / latte / cappuccino.

Item unavailable

![](https://i.imgur.com/IXtcqdD.png)

If you choose an item that is unavailable, the program asks for a new input.

All items unavailable

![](https://i.imgur.com/hsGaHMG.png)

If all items from menu are unavailable (due to lack of resources), this message will show up.

Payment - denied & success w/o change

![](https://i.imgur.com/H9OpqLk.png)

When you procceed to make a valid order, the payment part is started. If you fail to meet the cost of the chosen beverage, the order is cancelled. If not, it procceeds to make the beverage ordered and provide change (if necessary).

Payment - success w/ change

![](https://i.imgur.com/aEHcWQb.png)

Example of payment with change.

Admin functions

![](https://i.imgur.com/eWvNeKf.png)

On the main screen, you can use the admin functions to check for resource levels and/or turn off the machine for maintenance. The 'off' command closes the program.

