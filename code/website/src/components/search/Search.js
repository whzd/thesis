import React, { Component } from 'react';
import { Input, Button } from 'antd';
import { SearchOutlined } from '@ant-design/icons';
import './Search.css';

class Search extends Component {

    state = {
        term: ''
    };

    handleChange = (event) => {
        this.setState({
            term: event.target.value
        });
    };

    handleSubmit = event => {
        this.props.handleFormSubmit(this.state.term);
        return false;
    }

    render() {
        return (
            <div className="Search">
            <Input.Search style={{ width: '40%' }} placeholder='Pesquisa' size="large" onChange={this.handleChange} onSearch={this.handleSubmit} enterButton/>
            </div>
        )
    }
}

export default Search;
