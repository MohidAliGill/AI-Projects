female(pam).
female(liz).
female(ann).
male(bob).
male(pat).
male(jim).
male(tom).
male(joe).

parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
parent(joe,jim).

grandparent(X,Y):-
    parent(X,Z),
    parent(Z,Y).

child(X,Y):-
    parent(X,Y).

grandchild(X,Y):-
    parent(X,Z),
    child(Z,Y).
