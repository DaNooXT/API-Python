| id | nome  | cidade        |
| -: | ----- | ------------- |
|  1 | João  | Três Passos   |
|  2 | Maria | Santo Augusto |
|  3 | Pedro | Três Passos   |
|  4 | Ana   | Ijuí          |


|  id | cliente_id | valor |
| --: | ---------: | ----: |
| 101 |          1 |   500 |
| 102 |          1 |   200 |
| 103 |          2 |   800 |
| 104 |          4 |   300 |

SELECT
    id,
    cliente_id,
    valor,
    valor - LAG(valor) OVER (ORDER BY id)
FROM pedidos