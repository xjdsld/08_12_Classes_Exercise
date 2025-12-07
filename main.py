from collections import deque

class Cafe:
    def __init__(self):
        self.orders_queue = deque()

    def enqueue(self, order):
        self.orders_queue.append(order)

    def dequeue(self):
        if len(self.orders_queue) > 0:
              order = self.orders_queue.popleft()
              print(f"Готове замовлення: {order}")
        else: 
            print("!")

    def is_empty(self):
        if len(self.orders_queue) == 0:
            print("Усі замовлення виконано")
    
queue = Cafe()

def at_the_queu(orders = []):

    for i in orders:
        queue.enqueue(i)
    
    while len(queue.orders_queue) > 0:
        queue.dequeue()  
        
    queue.is_empty()

at_the_queu(orders = ["Кава", "Чай", "Сендвіч", "Піцца", "Десерт"])