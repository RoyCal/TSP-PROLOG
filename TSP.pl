/*Definição dos nós e arestas.*/

edge(a, b, 5900).
edge(a, c, 6200).
edge(a, d, 7900).
edge(a, e, 5200).
edge(a, f, 4900).
edge(a, g, 6300).
edge(a, h, 8000).
edge(b, a, 6700).
edge(b, c, 6200).
edge(b, d, 4200).
edge(b, e, 4500).
edge(b, f, 7000).
edge(b, g, 5300).
edge(b, h, 5900).
edge(c, a, 7500).
edge(c, b, 5700).
edge(c, d, 9400).
edge(c, e, 4000).
edge(c, f, 4100).
edge(c, g, 10500).
edge(c, h, 650).
edge(d, a, 7500).
edge(d, b, 4300).
edge(d, c, 10200).
edge(d, e, 8500).
edge(d, f, 11600).
edge(d, g, 1900).
edge(d, h, 9800).
edge(e, a, 5200).
edge(e, b, 4700).
edge(e, c, 2200).
edge(e, d, 8400).
edge(e, f, 4000).
edge(e, g, 9500).
edge(e, h, 4100).
edge(f, a, 6700).
edge(f, b, 6500).
edge(f, c, 3600).
edge(f, d, 10200).
edge(f, e, 4000).
edge(f, g, 11200).
edge(f, h, 4400).
edge(g, a, 4900).
edge(g, b, 5600).
edge(g, c, 10100).
edge(g, d, 1900).
edge(g, e, 11800).
edge(g, f, 8900).
edge(g, h, 11100).
edge(h, a, 7900).
edge(h, b, 6100).
edge(h, c, 250).
edge(h, d, 9800).
edge(h, e, 4500).
edge(h, f, 3800).
edge(h, g, 10900).

/* Encontra o comprimento de uma lista. Enquanto houver algo na lista, incrementa N.
Quando não houver mais nada, ele retorna.*/

len([], 0).
len([H|T], N):- len(T, X), N is X+1 .

/*O melhor caminho é chamado por shortest_path. Ele envia os caminhos encontrados em um
formato de caminho e distância*/

best_path(Visited, Total):- path(a, a, Visited, Total).

/*O caminho é expandido para incluir a distância até o momento e os nós visitados*/

path(Start, Fin, Visited, Total) :- path(Start, Fin, [Start], Visited, 0, Total).

/*Adiciona o local de parada à lista visitada, adiciona a distância e então chama recursivamente
para o próximo local de parada ao longo do caminho */

path(Start, Fin, CurrentLoc, Visited, Costn, Total) :-
    edge(Start, StopLoc, Distance), NewCostn is Costn + Distance, \+ member(StopLoc, CurrentLoc),
    path(StopLoc, Fin, [StopLoc|CurrentLoc], Visited, NewCostn, Total).

/*Quando encontrarmos um caminho de volta ao ponto de partida, fazemos dessa a distância total e nos certificamos
de que tenhamos passado por todos os nós grafo*/

path(Start, Fin, CurrentLoc, Visited, Costn, Total) :-
    edge(Start, Fin, Distance), reverse([Fin|CurrentLoc], Visited), len(Visited, Q),
    (Q\=9 -> Total is 100000; Total is Costn + Distance).

/*Encontra o caminho mais curto, pega todos os caminhos e os reúne em Holder.
Em seguida, chama pick no Holder, que escolhe o caminho mais curto e o retorna.*/

shortest_path(Path):-setof(Cost-Path, best_path(Path,Cost), Holder),pick(Holder,Path).

/*Compara 2 distâncias. Se o custo for menor que Bcost, pode parar*/

best(Cost-Holder,Bcost-_,Cost-Holder):- Cost<Bcost,!.
best(_,X,X).

/*Pega o melhor caminho e a distância do Holder e o chama recursivamente.*/

pick([Cost-Holder|R],X):- pick(R,Bcost-Bholder),best(Cost-Holder,Bcost-Bholder,X),!.
pick([X],X).

