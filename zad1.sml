(*
 * Zadanie domowe 1, czesc 1
 *  structure file
 *)
(* structure id291529 :> PART_ONE =
struct
  exception NotImplemented *)

  datatype 'a tree= Leaf of 'a | Node of 'a tree * 'a * 'a tree

  (* suma liczb naturalnych od 1 do n *)
  fun sum (n:int) = if n=1 then 1
		else n+sum(n-1);
 
  (* silnia *)
  fun fac (n:int) = if n=1 then 1
		else n*fac(n-1);

  (* ciag Fibonacciego *)
  fun fib (n:int) = if n<=1 then 1
		else fib(n-1)+fib(n-2);
  
  (* NWD - algorytm Euklidesa *)
  fun gcd (m:int, n:int) = if m=0 then n
		else if n=0 then m
		else if m>n then gcd(n, m mod n) 
		else gcd(m, n mod m);
  
  (* maksimum max z listy *)
  fun max (l:int list) = case l of 
		nil => 0
		| head::nil => head 
		| head::tail => if head > max(tail) then head 
		else max(tail);
	
  (* suma liczb naturalnych przechowywanych w drzewie binarnym *)
  fun sumTree (t:int tree) = case t of
		Leaf l => l
		| Node (left, x, right) => sumTree(left) + x + sumTree(right); 
  
  (* glebokosc zagniezdzenia drzewa *)
  fun depth (t:'a tree) = case t of
		Leaf l => 0
		| Node (left, x, right) => if depth(left) > depth(right)  then 1 + depth(left)
		else 1 + depth(right); 
		
  (* szukanie elementu w drzewie *)
  fun binSearch (t:int tree)(n:int) = case t of
		Leaf l => if l=n then true 
			else false 
		| Node (left, y, right) => if y=n then true 
			else if n<y then binSearch left n
			else binSearch right n; 
		
  (* przejscie drzewa typu pre-order *)  
  fun preorder (t:'a tree) = case t of
		Leaf l => [l]
		| Node (left, x, right) => [x] @ preorder left @ preorder right; 

  (* dodawanie kazdej pary liczb calkowitych z 2 list *)
  fun listAdd (a:int list) [] = a
		| listAdd [] (b:int list) = b
		| listAdd (a:int list as ahead :: atail)(b:int list as bhead :: btail) = ahead+bhead :: listAdd atail btail;
		
  (* wkladanie elementu w posortowana liste *)
  fun insert (m:int) [] = [m]
		| insert (m:int) (l:int list as head :: tail) = 
				if m > head then head :: insert m tail
				else m::l;	
  
  (* sortowanie listy *)
  fun insort (l:int list) = case l of 
		nil => nil
		| head::tail => insert head (insort tail);
		
  (* skladanie 2 funkcji *)
  fun compose f g  = (fn x => g(f x));
  
  (* currowanie *)
  fun curry f x y = f(x,y);
  
  (* odcurrowanie *)
  fun uncurry f (x,y) = f x y;
  
  (* wywolywanie danej funkcji n razy *)
  fun multifun f n = if n=1 then (fn x => f x)
		else (fn x => f (( multifun f (n-1)) x ));
  
  (* funkcja bioraca liste pierwszych i elementow listy l *)
  fun ltake (l:'a list) (n:int) = case l of
		[] => []
		| head::tail => if n=0 then []
        else head::(ltake tail (n-1));
		  
  (* badanie listy *)
  fun lall f [] = true
		| lall f (l:'a list as head::tail) = if f(head)=false then false
			else lall f tail;
  
  (* konwertowanie jednej listy w druga *)
  fun lmap f [] = []
		| lmap f (l:'a list as head::tail) = f(head)::lmap f tail;
  
  (* odwracanie listy *)
  fun lrev [] = []
		| lrev (l:'a list as head::tail) = lrev (tail) @ [head];
  
  (* dobieranie w pary odpowiadajacych sobie elemntow 2 list *)
  fun lzip (a, []) = []
		| lzip ([], b) = []
		| lzip (a:'a list as ahead :: atail, b:'b list as bhead :: btail) = (ahead,bhead) :: lzip (atail, btail);
  
  (* rozdzielanie 1 listy na 2 *)
  fun split [] = ([],[])
		| split [a] = ([a],[])
		| split (headodd :: headeven :: tail) = let val (lo,le) = split tail in ((headodd :: lo), (headeven :: le)) end;
  
  (* generowanie iloczynu kartezjanskiego z 2 list *)
  fun cartprod [] [] = []
		| cartprod (l: 'a list) [] = []
		| cartprod [] (l: 'b list) = []
		| cartprod (l1:'a list as ahead :: atail) (l2:'b list as bhead :: btail) = 
				(ahead, bhead) :: (cartprod [ahead] btail) @ (cartprod atail (bhead :: btail));

end
