emlista :: Int -> Int -> Int -> [Int] -> Bool
emlista n ini fim lista | ini > fim = False
                        | (lista !! meio) > n = emlista n ini (meio - 1) lista
                        | (lista !! meio) < n = emlista n (meio + 1) fim lista
                        | otherwise = True
                        where meio = (ini + fim) `div` 2

foradalista :: [Int] -> Int -> [Int] -> Int -> [Int]
foradalista ss s qs q = [x | x <- ss, not (emlista x 0 (q - 1) qs)]

parastring :: [Int] -> String
parastring (h:t) = if length t > 0
                    then show h ++ " " ++ parastring t
                    else show h

main = do
    s' <- getLine
    let s = read s' :: Int
    ss' <- getLine
    let ss = map read (words ss') :: [Int]
    q' <- getLine
    let q = read q' :: Int
    qs' <- getLine
    let qs = map read (words qs') :: [Int]
    putStrLn(parastring $ foradalista ss s qs q)
