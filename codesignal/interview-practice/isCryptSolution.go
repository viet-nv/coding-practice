// https://app.codesignal.com/interview-practice/task/yM4uWYeQTHzYewW9H

func isCryptSolution(crypt []string, solution [][]string) bool {
    arr := make([]int64, len(crypt))
    for i := 0; i < len(crypt); i++ {
        s := crypt[i]
        temp := make([]string, len(s))
        for j := 0; j < len(solution); j++ {
            for k := 0; k < len(s); k++ {
                if string(s[k]) == solution[j][0] {
                    temp[k] = solution[j][1]
                }
            }
        }
        if temp[0] == "0" && len(temp) > 1 {
            return false
        }
        x := ""
        for j:=0; j < len(temp); j++ {
            x = x + temp[j]
        }
        n , _ := strconv.ParseInt(x,10, 64)
        arr[i] = n
    }
    return arr[0] + arr[1] == arr[2]
}
