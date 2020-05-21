import React, { Component } from 'react';
import 'antd/dist/antd.css';
import './App.css';
import Navbar from '../navbar/Navbar.js';
import Search from '../search/Search.js';
import Display from '../display/Display.js';
import Avatar from '../avatar/Avatar.js';
import { Layout, Row, Col } from 'antd';
import explanation from '../../apis/Explanation.js';

const { Header, Footer, Content } = Layout;

class App extends Component {

    state = {
        explanations: null
    }

    handleSubmit = async (conceptFromSearch) => {
        const response = await explanation.get('/search', {
            params: {
                query: conceptFromSearch
            }
        })
        console.log(response.data)
        this.setState({
            explanations: response.data,
        })
    };

    render() {
        return (
            <div className="App">
                <Layout className="layout">
                    <Header>
                        <Row>
                            <Col flex={1}><div className="logo" /></Col>
                            <Col flex={8}><h1> <b>E</b>xplicação <b>A</b>utomática de <b>C</b>onceitos </h1></Col>
                            <Col flex={1}><Navbar /></Col>
                        </Row>
                    </Header>
                    <Content style={{ padding: '0 50px' }}>
                        <div className="site-layout-content">
                            <Search handleFormSubmit={this.handleSubmit}/>
                            <br />
                            <br />
                            <Row justify="center">
                                <Col flex="1 1 200px"><Display content={this.state.explanations}/></Col>
                                <Col flex="0 1 300px"><Avatar show={this.state.explanations}/></Col>
                            </Row>
                        </div>
                    </Content>
                    <Footer style={{ textAlign: 'center' }}>GILT ©2016</Footer>
                </Layout>
            </div>
        )
    }
}

export default App;
