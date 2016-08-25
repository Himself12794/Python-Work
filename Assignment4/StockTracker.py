from array_queue import ArrayQueue
#Python Version 2.7.5

class StockTracker:
#set constructor as an empty object
	def __init__(self):
		self._total_qty = 0
		self._profit = 0.0
		self._arque = ArrayQueue()
		
#buy stock. quantity must be greater than 0 and price must be a floating point number otherwise error occurs
	def buy ( self, quantity, price ):
		assert ( quantity > 0 ), 'quantity needs to be a positive integer'
		assert ( price > 0 ), 'price needs to be a positive floating point number'
		assert ( type( price ) is float ), 'price needs to be a positive floating point number'
		self._arque.enqueue( ( quantity, price ) )
		self._total_qty += quantity
		
#sell stock. quantity must be greater than 0, price must be floating point number,
#quantity must be less than or equal to the quantity on hand other wise error occurs
	def sell ( self, quantity, price ):
		assert ( quantity > 0 ), 'quantity needs to be a positive integer'
		assert ( price > 0 ), 'price needs to be a positive floating point number'
		assert ( type( price ) is float ), 'type must be float'
		assert ( quantity <= self.getQuantityOnHand() ), 'quantity needs to be less than or equal to the total number of shares on hand'
		
		selling = 0		
		while quantity > 0:
			transaction = self._arque.dequeue()			#Deque value
			amount = transaction[ 0 ]					#Parse value
			value = transaction[ 1 ]
			
			if quantity >= amount:						#Make sure the specific transaction has enough to fill the order
				selling += amount * ( price - value ) 	#Calculate the profit
				self._total_qty -= amount				#Update remaining shares sell
			else:
				selling += quantity  * ( price - value )
				self._total_qty -= quantity
				self._arque.enqueue( ( amount - quantity, value ) ) #Re-add what is left of this transaction
				while self._arque.first() != ( amount - quantity, value ): #Send it back to the front
					self._arque.enqueue( self._arque.dequeue() )
				
			quantity -= amount
		
		self._profit += selling
		return 	selling

#returns total gain or loss since creating the empty object        
	def getProfit (self):
		return self._profit
	
#returns the quantity of shares on hand   
	def getQuantityOnHand (self):
		return self._total_qty

