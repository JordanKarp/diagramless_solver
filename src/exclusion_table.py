from value import Value

# The exclusion table is used to help determine which values are possible for a single square.
# When used in the Puzzle.check_options(), it analyzes each of the neighbors, one at a time,
# and determines what is NOT possible for that specific configuration.

EXCLUSION_TABLE = {
    'U1': {
        Value.BLACK: {Value.ACROSS, Value.EMPTY},
        Value.ACROSS: {Value.DOWN, Value.ACROSSDOWN},
        Value.DOWN: {Value.DOWN, Value.ACROSSDOWN, Value.BLACK},
        Value.ACROSSDOWN: {Value.DOWN, Value.ACROSSDOWN, Value.BLACK},
        Value.EMPTY: {Value.DOWN, Value.ACROSSDOWN},
        Value.UNKNOWN: {}
    },
    'U2': {
        Value.BLACK: {},
        Value.ACROSS: {},
        Value.DOWN: {Value.DOWN, Value.ACROSSDOWN, Value.BLACK},
        Value.ACROSSDOWN: {Value.DOWN, Value.ACROSSDOWN, Value.BLACK},
        Value.EMPTY: {},
        Value.UNKNOWN: {}
    },
    'U3': {
        Value.BLACK: {},
        Value.ACROSS: {},
        Value.DOWN: {Value.DOWN, Value.ACROSSDOWN},
        Value.ACROSSDOWN: {Value.DOWN, Value.ACROSSDOWN},
        Value.EMPTY: {},
        Value.UNKNOWN: {}
    },
    'D1': {
        Value.BLACK: {Value.DOWN, Value.ACROSSDOWN},
        Value.ACROSS: {Value.BLACK},
        Value.DOWN: {Value.ACROSS, Value.DOWN,
                     Value.ACROSSDOWN, Value.EMPTY},
        Value.ACROSSDOWN: {Value.ACROSS, Value.DOWN,
                           Value.ACROSSDOWN, Value.EMPTY},
        Value.EMPTY: {Value.BLACK},
        Value.UNKNOWN: {}
    },
    'D2': {
        Value.BLACK: {Value.DOWN, Value.ACROSSDOWN},
        Value.ACROSS: {},
        Value.DOWN: {Value.DOWN, Value.ACROSSDOWN},
        Value.ACROSSDOWN: {Value.DOWN, Value.ACROSSDOWN},
        Value.EMPTY: {},
        Value.UNKNOWN: {}
    },
    'D3': {
        Value.BLACK: {},
        Value.ACROSS: {},
        Value.DOWN: {Value.DOWN, Value.ACROSSDOWN},
        Value.ACROSSDOWN: {Value.DOWN, Value.ACROSSDOWN},
        Value.EMPTY: {},
        Value.UNKNOWN: {}
    },
    'L1': {
        Value.BLACK: {Value.DOWN, Value.EMPTY},
        Value.ACROSS: {Value.ACROSS, Value.ACROSSDOWN, Value.BLACK},
        Value.DOWN: {Value.ACROSS, Value.ACROSSDOWN},
        Value.ACROSSDOWN: {Value.ACROSS, Value.ACROSSDOWN, Value.BLACK},
        Value.EMPTY: {Value.ACROSS, Value.ACROSSDOWN},
        Value.UNKNOWN: {}
    },
    'L2': {
        Value.BLACK: {},
        Value.ACROSS: {Value.ACROSS, Value.ACROSSDOWN, Value.BLACK},
        Value.DOWN: {},
        Value.ACROSSDOWN: {Value.ACROSS, Value.ACROSSDOWN, Value.BLACK},
        Value.EMPTY: {},
        Value.UNKNOWN: {}
    },
    'L3': {
        Value.BLACK: {},
        Value.ACROSS: {Value.ACROSS, Value.ACROSSDOWN},
        Value.DOWN: {},
        Value.ACROSSDOWN: {Value.ACROSS, Value.ACROSSDOWN},
        Value.EMPTY: {},
        Value.UNKNOWN: {}
    },
    'R1': {
        Value.BLACK: {Value.ACROSS, Value.ACROSSDOWN},
        Value.ACROSS: {Value.ACROSS, Value.DOWN,
                       Value.ACROSSDOWN, Value.EMPTY},
        Value.DOWN: {Value.BLACK},
        Value.ACROSSDOWN: {Value.ACROSS, Value.DOWN,
                           Value.ACROSSDOWN, Value.EMPTY},
        Value.EMPTY: {Value.BLACK},
        Value.UNKNOWN: {}
    },
    'R2': {
        Value.BLACK: {Value.ACROSS, Value.ACROSSDOWN},
        Value.ACROSS: {Value.ACROSS, Value.ACROSSDOWN},
        Value.DOWN: {},
        Value.ACROSSDOWN: {Value.ACROSS, Value.ACROSSDOWN},
        Value.EMPTY: {},
        Value.UNKNOWN: {}
    },
    'R3': {
        Value.BLACK: {},
        Value.ACROSS: {Value.ACROSS, Value.ACROSSDOWN},
        Value.DOWN: {},
        Value.ACROSSDOWN: {Value.ACROSS, Value.ACROSSDOWN},
        Value.EMPTY: {},
        Value.UNKNOWN: {}
    }
}
