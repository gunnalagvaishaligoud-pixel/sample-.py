class Queue:
  def __init__(self,cap=3):
    self._front=0
    self._rare=-1
    self._a=[None for _ in range(cap)]
    self._c=0
  def peek(self):
    if self._c==0:
      return "No elements"
    return self._a[self._front]
  def enqueue(self,data):
    if self._c==len(self._a):
      print('overflow')
      return
    self._a[self._c]=data
    self._c+=1
  def rare(self):
    return self._a[self._c-1]
  def dequeue(self,data):
    if self._front == self._c:
      print("underflow")
      return
    data = self._a[self._front]
    self._front += 1
    return data
queue=Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.dequeue(20)
print(queue.peek())
print(queue.rare())
