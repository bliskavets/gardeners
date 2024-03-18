import React from 'react'
import ReactDOM from 'react-dom/client'
import {App} from './App'
import './index.css'

import {ChakraProvider} from '@chakra-ui/react'
import {BrowserRouter} from 'react-router-dom'


const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement)

root.render(
  <React.StrictMode>
    <ChakraProvider>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </ChakraProvider>
  </React.StrictMode>
)