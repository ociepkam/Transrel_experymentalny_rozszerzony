# Transrel_experymentalny_rozszerzony
Transrel z manipulacją eksperymentalną przetwarzania relacji, jej integracji oraz pamięci.

Bodźcami mogą być dowolne obiekty podstawiane za A, B i C na poniższych schematach. Najpierw pojawiają się wertykalnie dwie pary bodźców połączonych symbolami „/”, „\” albo „|”. Kolejne symbole oznaczają „lewy powyżej prawego” („prawy niżej lewego), „lewy niżej prawego” („prawy wyżej lewego”), „lewy dokładnie obok prawego” (i vice versa). Zatem „/” oraz „\” to relacje przeciwsymetryczne (trzeba kodować kierunek), a „|” to relacja symetryczna (nie trzeba kodować).

Pierwsza para to zawsze A/B albo A\B. Pierwszy czynnik eksperymentalny, „wiązania”, polega na tym, że w warunku wiązań, dla pary A/B losowane jest C\B albo A\C, a dla A\B losowane jest C/B albo A/C. W warunku bez wiązań, dla A/B losowane są B|C albo A|C, a dla A\B losowane są C|B albo C|A.

Po X s horyzontalnie pojawiają się trzy odpowiedzi, prezentowane przez Y s. W tym czasie trzeba wybrać odpowiedź. Interwał między kolejnymi próbami Z s (potrzebny pilotaż). Są trzy warunki poprawnej odpowiedzi (czynnik „integracja”): bodźce z dwu par, bodźce odwrócone z jednej pary, bodźce nieodwrócone z jednej pary. W warunku wiązań odpowiedzi zawierają symbole „/” albo „\”, ale nie „|”. Jedna błędna odpowiedź zawiera bodźce z dwu par, a druga z jednej pary. Przykłady odpowiedzi dla pary A/B i C\B (kolejność par losowa, tu mi się nie chciało losować):

Bodźce z dwu par (16) Bodźce odwrócone (16) Bodźce nieodwrócone (16)

C\A C/A B\C A\C C/B B/C A\C C/B C\B

C\A A\C B\C A\C B\C B/C A\C B\C C\B

C\A C/A C/B C/A C/B B/C C/A C/B C\B

C\A A\C C/B C/A B\C B/C C/A B\C C\B

C\A C/A A\B A\C A\B B/C A\C A\B C\B

C\A A\C A\B A\C B/A B/C A\C B/A C\B

C\A C/A B/A C/A A\B B/C C/A A\B C\B

C\A A\C B/A C/A B/A B/C C/A B/A C\B

A/C A\C C/B A\C B/A B\A A\C B/A A/B

A/C … … B\A … A/B

W warunku bez wiązań także jedna błędna odpowiedź zawiera bodźce z dwu par, a jedna z jednej pary. Jedna losowa błędna odpowiedź jest z „|”, a druga z „/” lub ”\”. Dla bodźców nieodwróconych i odwróconych poprawna odpowiedź zawsze dotyczy pary „I”. Przykłady dla A/B i C|B:

Bodźce z dwu par (16) Bodźce odwrócone (16) Bodźce nieodwrócone (16)

C\A C/A A|B A\C A|B B|C A\C A|B C|B

C\A A\C A|B A\C B|A B|C A\C B|A C|B

C\A C/A B|A C/A A|B B|C C/A A|B C|B

C\A A\C B|A C/A B|A B|C C/A B|A C|B

C\A C|A B/A A|C C\B B|C A|C C\B C|B

C\A A|C B/A A|C B/C B|C A|C B/C C|B

C\A C|A A\B A|C C/B B|C A|C C/B C|B

C\A A|C A\B A|C B\C B|C A|C B\C C|B

A/C C\A A|B A|C A\B B|C A|C A\B C|B

A/C … A|C B/A B|C A|C B/A C|B

C|A … B|C C|A … C|B

Ponieważ dla każdego warunku są 4 rodzaje par, dla każdego warunku są 64 unikalne próby.

W bieżącym eksperymencie dla każdego warunku losujemy 40 prób (z 64 możliwych, bez zwracania). X = 8 s, Y = 7 s, Z = 2 s. Łącznie 240 prób, kolejność prób w pełni losowa.

Ponieważ zadanie jest długie, podzielimy je na trzy części, po 80 prób na część.
