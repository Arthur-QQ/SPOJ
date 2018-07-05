import System.Random

powmod :: Integer -> Integer -> Integer -> Integer
-- powmod a b c = a ^ b mod c
powmod a b c | b == 0 = 1
             | even b = ((powmod a (div b 2) c) ^ 2) `mod` c
             | otherwise = (a * ((powmod a (div (b-1) 2) c) ^ 2)) `mod` c

is_prime :: Integer -> Int -> Integer -> String
is_prime n it random
    | n <= 3 = "YES"
    | it == 0 = "YES"
    | gcd random n /= 1 = "NO"
    | powmod random (n-1) n == 1 = is_prime n (it - 1) random
    | otherwise = "NO"


func n = do
    if n > 0 then do
        value' <- getLine
        let value = read value' :: Integer
        a <- randomRIO (2, value-1)
        putStrLn $ is_prime value 2 a
        func (n - 1)
    else
        return ""

main = do
    lines' <- getLine
    let lines = read lines' :: Int
    func lines
