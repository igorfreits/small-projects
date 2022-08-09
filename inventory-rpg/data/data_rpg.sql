/*!40101 SET NAMES utf8 */

;

/*!40014 SET FOREIGN_KEY_CHECKS=0 */

;

/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */

;

/*!40111 SET SQL_NOTES=0 */

;

DROP TABLE IF EXISTS inventory;

CREATE TABLE
    `inventory` (
        `id` int NOT NULL AUTO_INCREMENT,
        `name` varchar(20) NOT NULL,
        `type` varchar(10) NOT NULL DEFAULT 'item',
        `class` varchar(10) NOT NULL,
        `rarity` varchar(10) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE = InnoDB AUTO_INCREMENT = 4 DEFAULT CHARSET = utf8mb3;

INSERT INTO
    inventory(id, name, type, class, rarity)
VALUES
(
        1,
        'espada de madeira',
        'arma',
        'guerreiro',
        'comum'
    ), (
        2,
        'arco de graveto',
        'arma',
        'arqueiro',
        'comum'
    ), (
        3,
        'hp potion',
        'item',
        'potion',
        'comum'
    );