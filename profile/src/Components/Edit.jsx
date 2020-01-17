import React, { Component } from 'react';
import './layout/edit.css';
import axios from 'axios';
import { Route, Router, Link, Redirect } from 'react-router-dom';
import App from '../App'

class Edit extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      id: this.props.id,
      username: this.props.username,
      first_name: this.props.first_name,
      last_name: this.props.last_name,
      email: this.props.email,
      contact_no: this.props.contact_no,
      image: this.props.image,
    };
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  async handleSubmit(event) {
    event.preventDefault();
    /* { [event.target.name]: event.target.value } */
    await this.setState({
      first_name: event.target.elements.first_name.value || this.state.first_name,
      last_name: event.target.elements.last_name.value || this.state.last_name,
      email: event.target.elements.email.value || this.state.email,
      contact_no: event.target.elements.contact_no.value || this.state.contact_no,
      image: event.target.elements.image.value || this.state.image,
    });
    
    /* console.log(event.target.elements.contact_no.value); */
    console.log(this.state.contact_no);
    {/* <Route><Redirect to = '/'/></Route> */ }
    this.props.onGetData({...this.state});
    console.log('1');
    console.log({ ...this.state });
    
    /* axios.put('http://127.0.0.1:8000/users/api/v1/2/', event.target.value) */
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          First Name:
          <input name="first_name" placeholder={this.state.first_name} />
        </label>
        <p></p>
        <label>
          Last Name:
          <input name="last_name" placeholder={this.state.last_name}/>
        </label>
        <p></p>
        <label>
          E-mail:
          <input name="email" placeholder={this.state.email} />
        </label>
        <p></p>
        <label>
          Contact:
          <input name="contact_no" placeholder={this.state.contact_no} />
        </label>
        <p></p>
        <label>
          Image:
          <input name="image" placeholder={this.state.image} />
        </label>
        <p></p>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default Edit;