from ib.ext.Contract import Contract
from ib.ext.Order import Order
from ib.opt import Connection
import time


def error_handler(msg):
	print("Server Error:", msg)


def server_handler(msg):
	print("Server Msg:", msg.typeName, "-", msg)


def create_contract(symbol, sec_type, exch, prim_exch, curr):
	contract = Contract()
	contract.m_symbol = symbol
	contract.m_secType = sec_type
	contract.m_exchange = exch
	contract.m_primaryExch = prim_exch
	contract.m_currency = curr
	return contract


def create_order(order_type, quantity, action):
	order = Order()
	order.m_orderType = order_type
	order.m_totalQuantity = quantity
	order.m_action = action
	return order


if __name__ == "__main__":

	# definovani spojenia
	client_id = 12
	# order_id = 1
	port = 7496
	tws_conn = None

	try:
		tws_conn = Connection.create(port=port, clientId=client_id)
		tws_conn.connect()
		tws_conn.register(error_handler, 'Error')
		tws_conn.registerAll(server_handler)

		for i in range(0, 5):

			# zistenie order ID
			oid_file = open('OID.txt', 'r')
			oid = oid_file.read()
			oid_file.close()
			oid = int(oid) + 1

			# otvorenie pozicie
			contract = create_contract('SPY', 'STK', 'SMART', 'ARCA', 'USD')
			order = create_order('MKT', 1, 'BUY')
			tws_conn.placeOrder(oid, contract, order)

			# zatvorenie order ID
			oid_file = open('OID.txt', 'w')
			oid_file.write(str(oid))
			oid_file.close()

			time.sleep(2)

	finally:
		if tws_conn is not None:
			tws_conn.disconnect()
