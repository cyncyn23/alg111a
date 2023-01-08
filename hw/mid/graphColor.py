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