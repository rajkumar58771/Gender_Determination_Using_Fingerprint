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
  const [gender,setGender] = useState([]);
  // console.log(gender)
  useEffect(()=>{
    axios.get('/api/result')
    .then((response)=>{
      setGender(response.data)
      // console.log(response)
      // gateData()
      console.log('Data fetched')
    })
    .catch((error)=>{
      console.log(error)
    })
  })
  return (
    <>
      <h1>Gender</h1> 
      <h1 id = 'hel'> -</h1>
      <h1 id = 'hel1'> -</h1>
      <h1 id = 'hel2'> -</h1>
    </>
  )
}

export default App
