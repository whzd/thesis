import React, { Component } from 'react';
import { Input } from 'antd';

class Search extends Component {
    render() {
        return (
            <div className="Search">
            Search block
            <Input.Search placeholder="input search text" size="large" enterButton/>
            </div>
        )
    }
}

export default Search;
