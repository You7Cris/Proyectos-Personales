module.exports = {
    //presets: [['@babel/preset-env', {targets: {node: 'current'}}]],
    presets:[
        ['@babel/preset-env', { targets: { esmodules: true }}],
        // ['@babel/preset-env', { esmodules: true }],
        ['@babel/preset-react', { runtime: 'automatic' }],
    ],
};