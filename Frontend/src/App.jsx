// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <div>
//         <a href="https://vitejs.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.jsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }

// export default App


import React, { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [Gender,setGender] = useState([])
  useEffect(()=>{
    axios.get('/api/result')
    .then((response)=>{
      setGender(response.data)
      // gateData()
      // console.log('Data fetched')
    })
    .catch((error)=>{
      console.log(error)
    })
  },[Gender])
  return (
    <>
      <h1>data</h1>
      <p>Gender : {Gender.length}</p>
      {
        Gender.map((Gender,index)=>(
          <div>
            {Gender.data}
          </div>
        ))
      }
      
    </>
  )
}

export default App
