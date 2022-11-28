const Signer  = require('./v4/index');
const express = require('express')
var morgan    = require('morgan')

const signer  = new Signer();
const app     = express()
const port    = 3000

app.use(morgan('combined'))
app.post('/sign', (req, res) => {
    res.send({
        __data__: signer.sign(
            decodeURIComponent(req.query.data), 
            decodeURIComponent(req.query.input),
            req.query.timestamp
    )})
})

app.post('/init', (req, res) => {
    res.send({
        __data__: signer.init()
    })
})

app.listen(port, () => {
    console.log(`signer ready on 127.0.0.1:${port}`)
})