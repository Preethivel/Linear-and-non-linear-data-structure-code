def NumberOfIlsands(grid):
  def dfs(r,c):
    if r>=len(grid) or c>=len(grid[0]) or c<0 or r<0 or grid[r][c]=='0':
      return
    grid[r][c]='0'
    dfs(r+1,c)
    dfs(r,c+1)
    dfs(r-1,c)
    dfs(r,c-1)
  cnt=0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[r][c]=='1':
        cnt+=1
        dfs(i,j)
  return cnt
