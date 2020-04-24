import React, { Component } from 'react';
import { Input, Button } from 'antd';
import { SearchOutlined } from '@ant-design/icons';

class Search extends Component {

    state = {
        term: 'Default text'
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
            Search block
            <form onSubmit={this.handleSubmit} className='ui form'>
            <Input.Group compact>
            <Input style={{ width: '40%' }} placeholder={this.state.term} size="large" onChange={this.handleChange}/>
            <Button style={{ width: '10%' }} size="large" type="primary" onClick={this.handleSubmit} icon={<SearchOutlined />}>Search</Button>
            </Input.Group>
            </form>
            </div>
        )
    }
}

export default Search;
