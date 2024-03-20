import {memo} from 'react'

import {Route, Routes} from 'react-router-dom'
import HelloWorldPage from './pages/HelloWorldPage'
import ItemPage from './pages/ItemPage'


function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<HelloWorldPage />} />
      <Route path="/items/:itemId" element={<ItemPage />} />
    </Routes>
  )
}

export default memo(AppRouter)
