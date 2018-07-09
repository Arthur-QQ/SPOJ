s = gets.to_i
ss = gets.split.map {|x| x.to_i}
q = gets.to_i
qs = gets.split.map {|x| x.to_i}
resp = Array.new

ss.each do |x|
    ini = 0
    fim = q - 1
    while ini <= fim
        meio = (ini + fim) / 2
        if x > qs[meio]
            ini = meio + 1
        elsif x < qs[meio]
            fim = meio - 1
        else
            break
        end
    end
    if ini > fim
        resp << x
    end
end
resp.sort!
puts resp.join(" ")
