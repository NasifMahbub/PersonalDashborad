import React, { Component } from 'react';
import './App.css';
import axios from 'axios';
import Home from './Components/Home.js'
import Edit from './Components/Edit.js'

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  NavLink
} from "react-router-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.getData = this.getData.bind(this);
    this.state = {
      id: null,
      username: null,
      first_name: null,
      last_name: null,
      email: null,
      contact_no: null,
      image: null
    };
  }

  getData(data){
    this.setState({
      id: data.id, username: data.username,
      first_name: data.first_name, last_name: data.last_name,
      email: data.email, contact_no: data.contact_no, image: data.image
    });
  }

  async componentDidMount() {
    await axios.get('http://127.0.0.1:8000/users/api/v1/2/')
      .then(res => {
        const data = res.data;
        this.getData(data);
      });
  }

  render() {
    return (

      <div className="App">
      <header className = "App-header">
      {/* <div>
            <nav className = "App-nav">
              <ul>
                <li>
                  <p>Home</p>
                </li>
                
              </ul>
            </nav>
        </div> */}
        <Router>
          <div>
            <nav className = "App-nav">
            <NavLink className="App-navLink" to = '#'>Home</NavLink>
            <NavLink className="App-navLink" to = '#'>Edit</NavLink>
            </nav>
            
            {/* <Switch>
              <Route path="/edit">
                <Edit/>
              </Route>
              
            </Switch> */}
          </div>
        </Router>
        </header>

        <div className="App-body">
          <h1>Welcome</h1>
          <p>This is the personal dashboard of {this.state.username} </p>
          <p>Name: {this.state.first_name}  {this.state.last_name}</p>
          <p>Email: {this.state.email}</p>
          <p>Contact No: {this.state.contact_no}</p>

          <img src={this.state.image} alt="" />
          <p></p>
        </div>
      </div>
    );
  }
}

export default App;
