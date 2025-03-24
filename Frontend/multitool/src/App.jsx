import { useEffect, useState } from 'react'
import './App.css'
import axios from "axios";

function App() {

  const [items, setItems] = useState([])

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/items")
    .then((response) => {
     setItems(Object.values(response.data));
      console.log(response.data)
    }).catch((error) => {
      console.log("There was an error retrieving the todo list: ", error);
    });
  }, []);

  return (
    <>


      <ul>
        {items ? items.map((item, index) => (
          <li key={index}>
          <strong>ID: </strong> {item.id} <br />
          <strong>Name:</strong> {item.name} <br />
          <strong>Price:</strong> {item.price} <br />
          <strong>Date:</strong> {item.date} <br />
          <strong>Location X:</strong> {item.location?.x} <br />
          <strong>Location Y:</strong> {item.location?.y} <br />
          <hr />
          </li>
        )): "Loading...."}
      </ul>

      <div>
      <h2>Items Table</h2>
      {items.length > 0 ? (
        <table className="table-auto border-2" border="1">
          <thead>
            <tr className="border-2">
              <th>ID</th>
              <th>Name</th>
              <th>Price</th>
              <th>Date</th>
              <th>Location X</th>
              <th>Location Y</th>
            </tr>
          </thead>
          <tbody>
            {items.map((item) => (
              <tr className="border-2" key={item.id}>
                <td className="border-1">{item.id}</td>
                <td className="border-1">{item.name}</td>
                <td className="border-1">{item.price}</td>
                <td className="border-1">{item.date}</td>
                <td className="border-1">{item.location?.x}</td>
                <td className="border-1">{item.location?.y}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>Loading...</p>
      )}
    </div>

    </>
  )
}


export default App
