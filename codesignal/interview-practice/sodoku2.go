// https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn

func sudoku2(grid [][]string) bool {
    
    for i:= 0; i < len(grid);i+=3 {
        for j:=0; j < len(grid); j+=3 {
            
            arr:= make([]int, 10)
            for k := i; k < i+3; k++  {
                for l :=j; l< j+3;l++ {
                    
                    if grid[k][l] != "." {
                        n, _ := strconv.ParseInt(grid[k][l], 10, 0)
                        arr[n]++
                    }
                }
            }
           
            for k:=1; k<=9; k++ {
                if arr[k] > 1 {
                    return false
                }
            }
        }
        
        
    }
    
    for i:=0; i < len(grid); i++ {
        arr:= make([]int, 10)
        for j:=0; j < len(grid); j++ {
            if grid[i][j] != "." {
                n, _ := strconv.ParseInt(grid[i][j], 10, 0)
                arr[n]++
            }
        }
         for j:=1; j<=9; j++ {
            if arr[j] > 1 {
             return false
            }
        }
        
        
        arr2:= make([]int, 10)
        
        for j:=0; j < len(grid); j++ {
            if grid[j][i] != "." {
                n, _ := strconv.ParseInt(grid[j][i], 10, 0)
                arr2[n]++
            }
        }
         for j:=1; j<=9; j++ {
            if arr2[j] > 1 {
             return false
            }
        }
    }
    
    return true
}   
