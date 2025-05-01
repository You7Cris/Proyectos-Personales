const { processNode } = require('./processNode');

function processMultipleNode(nodes) {
    if(!Array.isArray(nodes)) {
        throw new Error('Los nodos no son válidos');
    }

    return nodes.map(node => processNode(node));
}

module.exports = { processMultipleNode };