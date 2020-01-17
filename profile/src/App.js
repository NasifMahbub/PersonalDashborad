import React, { Component } from 'react';
import './App.css';
import Home from './Components/Home.jsx'
import Edit from './Components/Edit.jsx'

import {
  BrowserRouter as Router,
  Switch,
  Route,
  NavLink
} from "react-router-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.storeGetData = this.storeGetData.bind(this);
    /* this.state = {
      id: "",
      username: "",
      first_name: "",
      last_name: "",
      email: "",
      contact_no: "",
      image: "",
    }; */

    this.state ={
      id: "2",
      username: "test1",
      first_name: "Nasif",
      last_name: "Mahbub",
      email: "test1@gmail.com",
      contact_no: "0",
      image: "profile_image/owl_qx5Urz9.png"
    }
  }

  /* async componentDidMount() {
    await axios.get('http://127.0.0.1:8000/users/api/v1/2/')
      .then(res => {
        const data = res.data;
        this.getData(data);
      });
  } */

  storeGetData(data){
    console.log('storegetdata called');
    console.log(data);
    this.setState({
      id: data.id, username: data.user_name,
      first_name: data.first_name, last_name: data.last_name,
      email: data.email_address, contact_no: data.contact_no, image: data.image
    });
  }
  componentDidMount(){
    console.log(this.props.contact_no);
  }

  render() {
    return (
      <div className="App">
      <header className = "App-header">
        <Router>
          <div>
            <nav className = "App-nav">
            <NavLink className="App-navLink" to = '/'>Home</NavLink>
            <NavLink className="App-navLink" to = '/edit'>Edit</NavLink>
            </nav>
            
            <Switch>  
              <Route path="/edit">
                <Edit onGetData={this.storeGetData} {...this.state}/>
              </Route>
              <Route path="/" >
                <Home onGetData={this.storeGetData} {...this.state}/>
              </Route>
            </Switch>
          </div>
        </Router>
        </header>
      </div>
    );
  }
}

export default App;
