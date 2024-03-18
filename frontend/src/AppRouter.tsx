import {memo} from 'react'

import {Route, Routes} from 'react-router-dom'
import HelloWorldPage from './pages/HelloWorldPage'


function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<HelloWorldPage />} />
    </Routes>
  )
}

export default memo(AppRouter)
