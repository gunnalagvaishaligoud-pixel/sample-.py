class Queue:
  def __init__(self,cap=3):
    self._front=0
    self._rare=-1
    self._a=[None for _ in range(cap)]
    self._c=0

  def is_empty(self):
    return self._c == 0

  def is_full(self):
    return self._c == len(self._a)

  def peek(self):
    if self._c==0:
      return "NO ELEMENTS"
    return self._a[self._front]

  def enqueue(self,data):
    if self._c==len(self._a):
      print('over flow')
      return
    self._a[self._c]=data
    self._c+=1

  def rare(self):
    return self._a[self._c-1]

  def dequeue(self):
    ar=[None for _ in range(len(self._a))]
    for i in range(1,self._c):
      ar[i-1]=self._a[i]
    self._c-=1
    temp=self._a[self._front]
    self._a=ar
    return temp


queue=Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.is_empty())
print(queue.is_full())
print(queue.dequeue())
queue.enqueue(40)
print(queue.peek())
print(queue.rare())