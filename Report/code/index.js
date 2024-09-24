// Requirements
const express = require('express')
const serveIndex = require('serve-index')
const bodyParser = require('body-parser')
require('dotenv').config()
const app = express()

// Variables
const port = process.env.PORT || 5000

// Parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({'extended': 'true'}))

// Parse application/json
app.use(bodyParser.json())

// Parse application/vnd.api+json as json
app.use(bodyParser.json({ type: 'application/vnd.api+json' }))

// Serve static assets
app.use('/assets', express.static('assets'), serveIndex('assets', {'icons': true}))

// Firebase
let firebase = require('./services/firebase.service')
firebase.initializeApp()

// Routes
require('./routes.js')(app)

app.listen(port, () => console.log('Webhook server is listening on port ' + port))