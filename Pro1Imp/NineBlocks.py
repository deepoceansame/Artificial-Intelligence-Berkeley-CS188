import heapq


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.

      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """

    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        pair = (priority, item)
        heapq.heappush(self.heap, pair)

    def pop(self):
        (priority, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0


class PriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and the Stack classes. This is designed for drop-in replacement for
    those two classes. The caller has to provide a priority function, which
    extracts each item's priority.
    """

    def __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction  # store the priority function
        PriorityQueue.__init__(self)  # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))


class NineBlocksState:
    def __init__(self, matrix, acu_op, cost):
        self.id = ''
        self.matrix = matrix
        self.acu_op = acu_op
        self.cost = cost
        for i in range(3):
            for j in range(3):
                self.id += str(matrix[i][j])

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def getSuccessors(self):
        lis = []
        a = 0
        b = 0
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == 0:
                    a = i
                    b = j
                    break
        if a - 1 >= 0:
            mat = [[0 for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    mat[i][j] = self.matrix[i][j]
            mat[a][b] = self.matrix[a - 1][b]
            mat[a - 1][b] = 0
            acu_op = list(self.acu_op)
            acu_op.append('n')
            st = NineBlocksState(mat, acu_op, self.cost + 1)
            lis.append(st)

        if b - 1 >= 0:
            mat = [[0 for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    mat[i][j] = self.matrix[i][j]
            mat[a][b] = self.matrix[a][b - 1]
            mat[a][b - 1] = 0
            acu_op = list(self.acu_op)
            acu_op.append('w')
            st = NineBlocksState(mat, acu_op, self.cost + 1)
            lis.append(st)

        if a + 1 < 3:
            mat = [[0 for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    mat[i][j] = self.matrix[i][j]
            mat[a][b] = self.matrix[a + 1][b]
            mat[a + 1][b] = 0
            acu_op = list(self.acu_op)
            acu_op.append('s')
            st = NineBlocksState(mat, acu_op, self.cost + 1)
            lis.append(st)

        if b + 1 < 3:
            mat = [[0 for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    mat[i][j] = self.matrix[i][j]
            mat[a][b] = self.matrix[a][b + 1]
            mat[a][b + 1] = 0
            acu_op = list(self.acu_op)
            acu_op.append('e')
            st = NineBlocksState(mat, acu_op, self.cost + 1)
            lis.append(st)

        return lis

    def getHValue(self):
        hvalue = 0
        t: int = 0
        a: int = 0
        b: int = 0
        for i in range(3):
            for j in range(3):
                t = self.matrix[i][j]
                if t != 0:
                    a = t // 3
                    b = t % 3
                    hvalue += abs(i - a) + abs(j - b)
        return hvalue

    def isGoalState(self):
        return self.id == '012345678'

    def __lt__(self, other):
        return True


def searchForNineBlocks(firstState: NineBlocksState):
    co = 0
    que = PriorityQueue()
    que.push(firstState, 0)
    pop_state = None
    visited_state = set()
    while not que.isEmpty():
        pop_state = que.pop()
        co = co+1
        if pop_state.isGoalState():
            break
        visited_state.add(pop_state)
        for st in pop_state.getSuccessors():
            if st not in visited_state:
                que.push(st, st.cost+st.getHValue())
    print(pop_state.acu_op)
    print(pop_state.cost)
    print(co)

'''
ma = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
mb = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
stateA = NineBlocksState(ma, [], 0)
stateB = NineBlocksState(mb, [], 0)
li = [stateA]
print(stateB.__eq__(stateA))
lis = stateA.getSuccessors()
for s in lis:
    print(s.matrix)
    print(s.acu_op, s.cost)
print()
lis = stateB.getSuccessors()
for s in lis:
    print(s.matrix)
    print(s.acu_op, s.cost)
print(stateA.getHValue())
print(stateB.getHValue())
print(stateA.isGoalState())
print(stateB.isGoalState())
que = PriorityQueue()
que.push(stateA, 0)
que.push(stateB, 1)
print(que.pop().id)
print(que.pop().id)
'''


mc = [[1, 2, 0], [5, 3, 4], [8, 6, 7]]
stateC = NineBlocksState(mc, [], 0)
searchForNineBlocks(stateC)

