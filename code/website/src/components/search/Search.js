import React, { Component } from 'react';
import { Input, Button } from 'antd';
import { SearchOutlined } from '@ant-design/icons';
import './Search.css';

class Search extends Component {

    state = {
        term: 'Pesquisa'
    };

    handleChange = (event) => {
        this.setState({
            term: event.target.value
        });
    };

    handleSubmit = event => {
        event.preventDefault();
        this.props.handleFormSubmit(this.state.term);
    }

    render() {
        return (
            <div className="Search">
            <form onSubmit={this.handleSubmit} className='ui form'>
            <Input.Search style={{ width: '40%' }} placeholder={this.state.term} size="large" onChange={this.handleChange} enterButton/>
            </form>
            </div>
        )
    }
}

export default Search;
