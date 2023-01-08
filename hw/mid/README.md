## Grapg coloring 
(自行尋找問題 : WIKI - List of NP-complete problems)

[Coloring](https://web.ntnu.edu.tw/~algo/Coloring.html#1)

### Example
### k-Vertex Coloring
k 點著色 : 使用 k 種顏色完成點著色。 NP-complete 。
特殊圖可推理出最小著色數的上限。
![x(G)](https://github.com/cyncyn23/alg111a/blob/main/hw/mid/x(G).jpg)
![kVertex](https://github.com/cyncyn23/alg111a/blob/main/hw/mid/kVertex.jpg)
### Greedy Vertex Coloring / Grundy Chromatic Number
```
「貪心點著色」是採用貪心法而得到的點著色，可能有許多種。「 Grundy 著色數」是貪心點著色的顏色數目。不控制著色數。
最小點著色、 k 點著色，都是 NP-complete 問題，沒有快速的演算法。於是有些人轉為討論貪心點著色，設計快速的演算法。
```

### 無向圖點著色（ Welsh–Powell Algorithm ）
```
貪心點著色。圖上每個點，依照邊數由大到小排序，依序塗色。針對一個點，依序嘗試各種顏色，直到不牴觸已塗色的點。
每個點的邊數是 0 到 V-1 （不考慮多重的邊、不考慮自己連向自己的邊），排序可以採用 Counting Sort ，時間複雜度 O(V) 。
時間複雜度等於一次 Graph Traversal 的時間。圖的資料結構為 Adjacency Matrix 是 O(V²) ，圖的資料結構為 Adjacency Lists 是 O(V+E) 。
```

![welsh](welshPowell.jpg)

### 貪婪法
貪婪著色 依次考慮圖的頂點，並為每個頂點分配其第一個可用顏色，

即以特定順序考慮頂點 v1, v2, … vn， 和 vi 並分配了未被任何人使用的最小可用顏色 vi的鄰居。

對於最大度數圖 x, 貪心著色最多會使用 x+1 顏色。貪婪的著色可以是任意的；
```
ex: 一個完整的二分圖，有 n 頂點，可以是 2 色，

但貪婪著色導致 n/2 顏色。
```

## Code
```py
# 表示圖對象的類
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
 
        # 向無向圖添加邊
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# 函數將顏色分配給Graph的頂點
def colorGraph(graph, n):
 
    # 跟踪分配給每個頂點的顏色
    result = {}
 
    # 給頂點一個一個分配顏色
    for u in range(n):
 
        # 檢查 `u` 的相鄰頂點的顏色並將它們存儲在一個集合中
        assigned = set([result.get(i) for i in graph.adjList[u] if i in result])
 
        # 檢查第一個自由顏色
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1
 
        # 為頂點`u`分配第一個可用顏色
        result[u] = color
 
    for v in range(n):
        print(f'Color assigned to vertex {v} is {colors[result[v]]}')
 
 
# Graph的貪婪著色
if __name__ == '__main__':
 
    # 為具有更多頂點的Graphs形添加更多顏色
    colors = ['', 'BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK',
            'BLACK', 'BROWN', 'WHITE', 'PURPLE', 'VOILET']
 
    # 上圖的圖邊列表
    edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
 
    # 圖中的節點總數(標記為0到5)
    n = 6
 
    # 從給定的邊構建圖
    graph = Graph(edges, n)
 
    # 使用貪心算法的#彩色圖
    colorGraph(graph, n)
```
## Result
```powershell
PS C:\Users\user\Desktop\Github\cynthia1231\alg111a\hw\mid> python graphColor.py
Color assigned to vertex 0 is BLUE
Color assigned to vertex 1 is GREEN
Color assigned to vertex 2 is BLUE
Color assigned to vertex 3 is RED
Color assigned to vertex 4 is RED
Color assigned to vertex 5 is GREEN

```