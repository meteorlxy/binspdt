'''
@reference [https://blog.csdn.net/thundermrbird/article/details/52231639]
@reference [https://blog.csdn.net/pi9nc/article/details/12250247]
@reference [http://dingdongsheng.cool.blog.163.com/blog/static/1186187552009431405995/]
@reference [http://csclab.murraystate.edu/~bob.pilgrim/445/munkres.html]

KM算法是通过给每个顶点一个标号（叫做顶标）来把求最大权匹配的问题转化为求完备匹配的问题的。
设顶点Xi的顶标为A[i]，顶点Yi的顶标为B[i]，顶点Xi与Yj之间的边权为w[i,j]。在算法执行过程中
的任一时刻，对于任一条边(i,j)，A[i]+B[j]>=w[i,j]始终成立。

KM算法的正确性基于以下定理：

若由二分图中所有满足A[i]+B[j]=w[i,j]的边(i,j)构成的子图（称做相等子图）有完备匹配，那么
这个完备匹配就是二分图的最大权匹配。

这个定理是显然的。因为对于二分图的任意一个匹配，如果它包含于相等子图，那么它的边权和等于所
有顶点的顶标和；如果它有的边不包含于相等子图，那么它的边权和小于所有顶点的顶标和。所以相等
子图的完备匹配一定是二分图的最大权匹配。

初始时为了使A[i]+B[j]>=w[i,j]恒成立，令A[i]为所有与顶点Xi关联的边的最大权，B[j]=0。如果
当前的相等子图没有完备匹配，就按下面的方法修改顶标以使扩大相等子图，直到相等子图具有完备匹
配为止。

我们求当前相等子图的完备匹配失败了，是因为对于某个X顶点，我们找不到一条从它出发的交错路。这
时我们获得了一棵交错树，它的叶子结点全部是X顶点。现在我们把交错树中X顶点的顶标全都减小某个
值d，Y顶点的顶标全都增加同一个值d，那么我们会发现：

两端都在交错树中的边(i,j)，A[i]+B[j]的值没有变化。也就是说，它原来属于相等子图，现在仍属于
相等子图。

两端都不在交错树中的边(i,j)，A[i]和B[j]都没有变化。也就是说，它原来属于（或不属于）相等子图，
现在仍属于（或不属于）相等子图。

X端不在交错树中，Y端在交错树中的边(i,j)，它的A[i]+B[j]的值有所增大。它原来不属于相等子图，现
在仍不属于相等子图。

X端在交错树中，Y端不在交错树中的边(i,j)，它的A[i]+B[j]的值有所减小。也就说，它原来不属于相等
子图，现在可能进入了相等子图，因而使相等子图得到了扩大。

现在的问题就是求d值了。为了使A[i]+B[j]>=w[i,j]始终成立，且至少有一条边进入相等子图，d应该等
于min{A[i]+B[j]-w[i,j]|Xi在交错树中，Yi不在交错树中}。

以上就是KM算法的基本思路。但是朴素的实现方法，时间复杂度为O(n4)——需要找O(n)次增广路，每次增广
最多需要修改O(n)次顶标，每次修改顶标时由于要枚举边来求d值，复杂度为O(n2)。实际上KM算法的复杂
度是可以做到O(n3)的。我们给每个Y顶点一个“松弛量”函数slack，每次开始找增广路时初始化为无穷大。
在寻找增广路的过程中，检查边(i,j)时，如果它不在相等子图中，则让slack[j]变成原值与A[i]+B[j]-w[i,j]的
较小值。这样，在修改顶标时，取所有不在交错树中的Y顶点的slack值中的最小值作为d值即可。但还要注
意一点：修改顶标后，要把所有不在交错树中的Y顶点的slack值都减去d。
'''
import sys
import numpy as np

INF = float('inf')

class KM(object):
  '''
  KM Algorithm
  ====================================
  Example:
    km = KM([
      [2, 1, 3, 0],
      [3, 0, 4, 0],
      [0, 0, 5, 6],
    ])
    result = km.run()
    print(result)
  
  Result:
    {'x': array([2, 0, 3]), 'y': array([ 1, -1,  0,  2])}
  ====================================
  Default dtype is int, and will tranfrom all the weights into integers
  If you need float weights, set dtype=float
  (see [https://docs.scipy.org/doc/numpy/user/basics.types.html])
  Example:
    km = KM([
      [2.5, 1.0, 3.3, 0],
      [3.6, 0, 4.4, 0],
      [0, 0, 5.5, 6.6],
    ], float)
  ====================================
  '''
  def __init__(self, matrix, dtype=int):
    # 输入权重矩阵
    if isinstance(matrix, np.ndarray):
      self.matrix = matrix.copy()
    else:
      self.matrix = np.array(matrix, dtype)
    # 获取权重矩阵行数x和列数y，保证x不大于y
    self.div_x, self.div_y = self.matrix.shape
    # 若x>y，则转置
    self.is_transpose = self.div_x > self.div_y 
    if self.is_transpose:
      self.matrix = np.transpose(self.matrix)
      self.div_x, self.div_y = self.matrix.shape
    # 用来记录每轮x和y的顶标
    self.label_x = np.zeros(self.div_x, dtype)
    self.label_y = np.zeros(self.div_y, dtype)
    # 用来记录每轮x和y是否被匹配
    self.selected_x = np.zeros(self.div_x, np.bool_)
    self.selected_y = np.zeros(self.div_y, np.bool_)
    # 记录y顶点的松弛量slack
    self.slack_y = np.ones(self.div_y) * INF
    # 记录y顶点的匹配结果，-1代表没有匹配
    self.match_y = np.ones(self.div_y, np.int_) * -1
    # 标记是否已经完成计算
    self.done = False
    # 存放计算结果
    self.result = None
    # 设置最大递归深度
    sys.setrecursionlimit(self.div_y)
  
  def run(self):
    '''
    Run the KM algorithm and return the result
    '''
    if not self.done:
      # 初始化顶标，权重都集中到x上
      for x in range(self.div_x):
        self.label_x[x] = max(self.matrix[x])
      # 遍历每一个x进行匹配
      for x in range(self.div_x):
        # 初始slack为无穷
        self.slack_y = np.ones(self.div_y) * INF
        while True:
          # 每轮初始，x和y都重置为没有匹配过
          self.selected_x = np.zeros(self.div_x, np.bool_)
          self.selected_y = np.zeros(self.div_y, np.bool_)

          # 如果顺利找到结果，结束，进入下一个x
          if self.dfs(x):
            break

          # 如果没有找到结果

          # 取所有未参与本轮匹配的y的slack值中的最小值作为d值
          d = INF
          for y in range(self.div_y):
            if (not self.selected_y[y]) and d > self.slack_y[y]:
              d = self.slack_y[y]
          
          if d != INF:
            for i in range(self.div_y):
              if i < self.div_x and self.selected_x[i]:
                # 对每个参与匹配的x，顶标减去d
                self.label_x[i] -= d
              if self.selected_y[i]:
                # 对每个参与匹配的y，顶标加上d
                self.label_y[i] += d
              else:
                # 对没有参与匹配的y，slack减去d
                self.slack_y[i] -= d
      # 标记计算已完成
      self.done = True
    return self.__generate_result()

  def dfs(self, x):
    '''
    Find the match y for the given x
    '''
    # 因为是从当前x开始找匹配，所以标记当前x已参与本轮匹配
    self.selected_x[x] = True
    # 遍历y寻找当前x本轮的匹配
    for y in range(self.div_y):
      # 如果y已经参与本轮匹配，跳过
      if self.selected_y[y]:
        continue
      # 如果y尚未参与本轮匹配，判断x和y间权重是否等于顶标和
      t = self.label_x[x] + self.label_y[y] - self.matrix[x][y]
      if t == 0:
        # 如果权重等于顶标和，则当前x和y可以匹配，标记y已参与本轮匹配
        self.selected_y[y] = True
        if self.match_y[y] == -1 or self.dfs(self.match_y[y]):
          # 若当前y还没有匹配的x，或者可以为当前y原匹配的x，找到一个新的匹配y
          # 则记当前x为当前y的匹配结果，即当前x已找到匹配
          self.match_y[y] = x
          return True
      elif self.slack_y[y] > t:
        self.slack_y[y] = t
    return False
  
  def __generate_result(self):
    if self.done and self.result == None:
      match_x = np.ones(self.div_x, np.int_) * -1
      for y in range(self.div_y):
        if self.match_y[y] != -1:
          match_x[self.match_y[y]] = y

      result_x, result_y = (match_x, self.match_y) if not self.is_transpose else (self.match_y, match_x)
      self.result = {
        'x': result_x.tolist(),
        'y': result_y.tolist(),
      }
    return self.result
