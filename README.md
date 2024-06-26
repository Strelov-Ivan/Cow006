# Test2
'Корова 006' coding
## Правила игры:
Для игры используется колода из 104 карт с уникальными значениями от 1 до 104. 
В игру можно играть компанией от 2 до 10 человек.
Для начала игры колода перемешивается, 4 верхние карты помещаются друг под другом - они будут служить игровым полем.
Затем каждому игроку раздаётся 10 карт. В итоге каждый тур состоит из 10 ходов.
В начале каждого тура игроки выбирают по одной карте из руки и кладут её рубашкой верх.
Как только все игроки выбрали карту, все карты открываются и помещаются на игровое поле в соответствии с несколькими правилами:
1) Карты в ряду должны идти по возрастанию.
2) Вы должны выбрать ряд, где разница между вашей картой и последней в ряду минимальная.
3) Если ваша карта оказалась шестой в ряду, вы забираете все карты в этом ряду, за исключением вашей разыгранной карты (она будет новой верхней картой этого ряда), и взятые вами карты записываются в штрафные очки.
4) Если вы не можете положить выбранную карту из-за того, что она меньше всех последних карт в рядах, вы выбираете ряд, который забираете себе, и оставляете вашу карту как верхнюю.
5) Порядок разыгрывания карт определяется их значением - игроки, которые положили наименьшие карты, разыгрывают эти карты первыми.

Победителем будет тот игрок, который получил наименьшее количество штрафных очков в ходе игры.
Для более продолжительной игры, можно начать новый тур, когда у всех игроков заканчиваются карты.
В конце каждого тура все игроки считают свои штрафные очки. Затем все карты перемешиваются и снова раздаются.
Тогда проигравшим будет игрок, который первым набрал 66 штрафных очков, а победитель - набравший наименьшее количество.

## Текстовый интерфейс
Пусть есть два игрока: Cow005, Cow006

```
Field: 
12 
57
34 35 37
7
Cow005: 38 39 48 56 74 84 89 98 100
Points = 0
Cow005 play 38
-----
Field: 
12 
57
34 35 37
7
Cow006: 1 6 32 44 46 59 65 73 89
Points = 0
Cow006 play 44
-----
Field: 
12 
57
34 35 37
7
Cow005 played 38
Cow006 played 44
New Field:
12 
57
34 35 37 38 44
7
-----
Field: 
12 
57
34 35 37 38 44
7
Cow005: 39 48 56 74 84 89 98 100
Points = 0
Cow005 play 48
-----
Field: 
12 
57
34 35 37 38 44
7
Cow006: 1 6 32 46 59 65 73 89
Points = 0
Cow006 play 46
-----
Field: 
12 
57
34 35 37 38 44
7
Cow006 played 46
Cow005 played 48
New Field:
12 
57
46 48
7
Cow006 took 34 35 37 38 44
-----
Field:
12 
57
46 48
7
Cow005: 39 56 74 84 89 98 100
Points = 0
Cow005 play 39
-----
Field:
12 
57
46 48
7
Cow006: 1 6 32 59 65 73 89
Points = 7
Cow006 play 1
-----
Field:
12 
57
46 48
7
Cow006 played 1
Cow005 played 39
Cow006 choose row 4
Cow006 took 7
New Field:
12 39
57
46 48
1
-----
Field:
12 39
57
46 48
1
Cow005: 56 74 84 89 98 100
Points = 0
Cow005 play 74
-----
Field:
12 39
57
46 48
1
Cow006: 6 32 59 65 73 89
Points = 8
Cow006 play 6
....
-----
Final Points:
Cow005: 8
Cow006: 20
Winner: Cow005!
```

## Пример save-файла
```json
{
    "field": [
        {
            "index": "0",
            "Cards": "12, 39"
        },
        {
            "index": "1",
            "Cards": "57"
        },
        {
            "index": "2",
            "Cards": "46, 48"
        },
        {
            "index": "3",
            "Cards": "1"
        }
    ],
    "players": [
        {
            "name": "Cow005",
            "Hand": "56 74 84 89 98 100",
            "Points": "0"
        },
        {
            "name": "Cow006",
            "Hand": "6 32 59 65 73 89",
            "Points": "8"
        }
    ]
}
```