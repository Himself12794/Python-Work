from StockTracker import StockTracker
from csc220a4TestData import data

def closeTo (a, b):
	return abs (a - b) < 0.05

def checkCreation (id):
	try:
		s = StockTracker ()
		if not closeTo (s.getProfit (), 0.0):
			print ('Test %d failed: StockTracker created with non-default value.' % id)
			return 0
		if not s.getQuantityOnHand () == 0:
			print ('Test %d failed: StockTracker created with non-default value.' % id)
			return 0
		print ('Test %d passed.' % id)
		return 1
	except:
		print ('Test %d failed: StockTracker created with unknown error.' % id)
		return 0

def buyInvalidQuantityTest (id, q):
	try:
		s = StockTracker ()
		s.buy (q, 12.34)
		print ('Test %d failed: no error with non-positive buying quantity.' % id)
		return 0
	except:
		if not closeTo (s.getProfit (), 0.0):
			print ('Test %d failed: buying error causes attribute change.' % id)
			return 0
		if not s.getQuantityOnHand () == 0:
			print ('Test %d failed: buying error causes attribute change.' % id)
			return 0
		print ('Test %d passed.' % id)
		return 1

def buyInvalidPriceTest (id, p):
	try:
		s = StockTracker ()
		s.buy (12, p)
		print ('Test %d failed: no error with non-positive buying price.' % id)
		return 0
	except:
		if not closeTo (s.getProfit (), 0.0):
			print ('Test %d failed: buying error causes attribute change.' % id)
			return 0
		if not s.getQuantityOnHand () == 0:
			print ('Test %d failed: buying error causes attribute change.' % id)
			return 0
		print ('Test %d passed.' % id)
		return 1

def sellInvalidQuantityTest (id, q):
	try:
		s = StockTracker ()
		s.sell (q, 12.34)
		print ('Test %d failed: no error with non-positive selling quantity.' % id)
		return 0
	except:
		if not closeTo (s.getProfit (), 0.0):
			print ('Test %d failed: selling error causes attribute change.' % id)
			return 0
		if not s.getQuantityOnHand () == 0:
			print ('Test %d failed: selling error causes attribute change.' % id)
			return 0
		print ('Test %d passed.' % id)
		return 1

def sellInvalidPriceTest (id, p):
	try:
		s = StockTracker ()
		s.buy (12, p)
		print ('Test %d failed: no error with non-positive selling price.' % id)
		return 0
	except:
		if not closeTo (s.getProfit (), 0.0):
			print ('Test %d failed: selling error causes attribute change.' % id)
			return 0
		if not s.getQuantityOnHand () == 0:
			print ('Test %d failed: selling error causes attribute change.' % id)
			return 0
		print ('Test %d passed.' % id)

		return 1

def buyingTest (id, st, quantity, price, totalShares, totalGain):
	try:
		st.buy (quantity, price)
		if not st.getQuantityOnHand () == totalShares:
			print ('Test %d failed: error in buying updates.' % id)
			return 0
		if not closeTo (st.getProfit (), totalGain):
			print ('Test %d failed: error in buying updates.' % id)
			return 0
		print ('Test %d passed.' % id)
		return 1
	except:
		print ('Test %d failed: unexpected error.' % id)
		return 0

def sellingTest (id, st, quantity, price, expectedResult, totalShares, totalGain):
	try:
		result = st.sell (quantity, price)
		if expectedResult is None:
			print ('Test %d failed: allow to sell more than enough.' % id)
			return 0
	except:
		if expectedResult is not None:
			print ('Test %d failed: unexpected error.' % id)
			return 0

	if not expectedResult is None:
		if not closeTo (expectedResult, result):
			print ('Test %d failed: return value mismatch - expecting %.2f, got %.2f.' % (id, expectedResult, result))
			return 0
	if not totalShares == st.getQuantityOnHand ():
		print ('Test %d failed: attribute update error - expecting %d, got %d.' % (id, totalShares, st.getQuantityOnHand ()))
		return 0
	if not closeTo (totalGain, st.getProfit ()):
		print ('Test %d failed: attribute update error - expecting %d, got %d.' % (id, totalGain, st.getProfit ()))
		return 0
	print ('Test %d passed.' % id)
	return 1

def test ():
	score = checkCreation (1)

	score += buyInvalidQuantityTest (2, 0)
	score += buyInvalidQuantityTest (3, -10)
	score += buyInvalidPriceTest (4, 0)
	score += buyInvalidPriceTest (5, -10.0)

	score += sellInvalidQuantityTest (6, 0)
	score += sellInvalidQuantityTest (7, -10)
	score += sellInvalidPriceTest (8, 0)
	score += sellInvalidPriceTest (9, -10.0)

	st = StockTracker ()

	for record in data:
		id, action, quantity, price, result, shares, gain = record
		#print( id, "buy" if action == 0 else "sell", quantity, price )
		if action == 0:
			score += buyingTest (id, st, quantity, price, shares, gain)
		else:
			score += sellingTest (id, st, quantity, price, result, shares, gain)
					
	print ('%d of 100 test cases passed - %.2f points.' % (score, score * 0.15))

def interfaceTest ():
	myDict = list ([item for item in list (StockTracker.__dict__) if item [0] != '_'])
	myDict.sort ()
	if not myDict == ['buy', 'getProfit', 'getQuantityOnHand', 'sell']:
		print ('Class interface error - too many or too few public elements')
		print ('Class interface score = 0.00')
	else:
		print ('Class interface score = 1.00')

test ()
interfaceTest ()




