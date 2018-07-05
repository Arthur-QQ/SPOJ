mainfunction n = do
    if n > 0 then do
        num <- getLine
        let s = sum [fromEnum x - 48 | x <- num]
        print(s)
        mainfunction (n-1)
    else
        return ""

main = do
    linhas' <- getLine
    let linhas = read linhas' :: Int
    mainfunction linhas
