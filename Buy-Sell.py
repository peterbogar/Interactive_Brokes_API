from ib.ext.Contract import Contract
from ib.ext.Order import Order
from ib.opt import Connection

import time
# import subprocess


def error_handler(msg):
	print('Server Error:', msg)


def server_handler(msg):
	print('Server Response:', msg.typeName, '-', msg)


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


def execute(symbol, sec_type, exch, prim_exch, curr, order_type, quantity, action):
	# zistenie order ID
	oid_file = open('OID.txt', 'r')
	oid = oid_file.read()
	oid_file.close()
	oid = int(oid) + 1

	# definovanie kontraktu
	contract = create_contract(symbol, sec_type, exch, prim_exch, curr)

	# definovanie orderu
	order = create_order(order_type, quantity, action)

	# odoslanie orderu
	tws_conn.placeOrder(oid, contract, order)
	time.sleep(20)  # pauza

	# update order ID
	oid_file = open('OID.txt', 'w')
	oid_file.write(str(oid))
	oid_file.close()


if __name__ == '__main__':

	client_id = 12
	port = 7496

	tws_conn = Connection.create(port=port, clientId=client_id)
	tws_conn.connect()
	tws_conn.register(error_handler, 'Error')
	# tws_conn.registerAll(server_handler)
	print('TWS connected')

	print(time.strftime('%d.%m.%Y %H:%M:%S'))
	# execute('AAPL', 'STK', 'SMART', 'NASDAQ', 'USD', 'MKT', '1', 'BUY')

	while True:
		datum_cas = time.strftime('%d.%m.%Y %H:%M')
		cas = time.strftime('%H:%M')
		minuty = time.strftime('%M')

		if minuty == '00':
			print(datum_cas)

		if cas == '20:55':
			print('Nakup SPY')
			# subprocess.call([r'c:\IBController\IBControllerGatewayStart.bat'])
			# time.sleep(60)
			print(datum_cas)
			execute('SPY', 'STK', 'SMART', 'ARCA', 'USD', 'MKT', '1', 'BUY')

		if cas == '07:00':
			print('Predaj SPY')
			# subprocess.call([r'c:\IBController\IBControllerGatewayStart.bat'])
			# time.sleep(60)
			print(datum_cas)
			execute('SPY', 'STK', 'SMART', 'ARCA', 'USD', 'MKT', '1', 'SELL')

		time.sleep(60)

	# tws_conn.disconnect()
