/**
 * Advent of Code, 2017 - Day 3
 */

/**
 * Data
 */
var data = 368078;

/**
 * PART 1
 */
function spiral1(input) {

    var ring = 1;
    while (ring * ring < input) {
        ring += 1;
    }

    ring = ring - (ring % 2);
    var offset = -(ring / 2);
    for (var i = (ring - 1) * (ring - 1) + 1; i <= input; i++) {
        if (offset === (ring - (ring % 2)) / 2) {
            offset = -offset;
        }
        offset++;
    }
    offset = Math.abs(offset);

    var dist = offset + ring / 2;
    console.log(input + " is " + dist + " steps away from the centre.");
}

spiral1(data);


/**
 * PART 2
 */
function spiral2(input) {
    var grid = {};

    grid['input'] = input;
    grid['answer'] = undefined;

    grid['x'] = 0;
    grid['y'] = 0;

    grid[grid['x']] = {};
    grid[grid['x']][grid['y']] = 1;

    for (var i = 0; grid['answer'] === undefined; i++) {
        step(grid, 'right');
        for (var j = 0; j < 2 * i + 1; j++) step(grid, 'up');
        for (var j = 0; j < 2 * i + 2; j++) step(grid, 'left');
        for (var j = 0; j < 2 * i + 2; j++) step(grid, 'down');
        for (var j = 0; j < 2 * i + 2; j++) step(grid, 'right');
    }

    console.log("The first number bigger than " + input + " is " + grid['answer'] + ".");



    function step(grid, direction) {
        if (grid['answer'] === undefined) {
            switch (direction) {
                case 'up':
                    grid['y']++;
                    break;
                case 'down':
                    grid['y']--;
                    break;
                case 'left':
                    grid['x']--;
                    break;
                case 'right':
                    grid['x']++;
                    break;
            }
            var num = 0;
            for (var i = -1; i <= 1; i++) {
                for (var j = -1; j <= 1; j++) {
                    if (grid[grid['x'] + i] !== undefined && grid[grid['x'] + i][grid['y'] + j] !== undefined) {
                        num += grid[grid['x'] + i][grid['y'] + j];
                    }
                }
            }

            if (grid[grid['x']] === undefined) {
                grid[grid['x']] = {};
            }

            grid[grid['x']][grid['y']] = num;
            if (grid[grid['x']][grid['y']] > input) {
                grid['answer'] = grid[grid['x']][grid['y']];
            }
        }
    }
}

spiral2(data);
