const Signer  = require('./v4/index');
const express = require('express')

const signer = new Signer();
const app    = express()
const port   = 3000


app.post('/sign', (req, res) => {
    console.log(req.query)
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
    console.log(`Example app listening on port ${port}`)
})