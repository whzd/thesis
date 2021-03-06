import React, { Component } from 'react';
import { Button, Card, Popconfirm, Tooltip, Spin } from 'antd';
import { PlayCircleOutlined, CameraOutlined, DislikeOutlined, LikeOutlined, InfoCircleOutlined } from '@ant-design/icons';
import Explanation from '../../apis/Explanation.js';
import i18n from '../../i18next';

function cancel(e) {
    console.log(e);
}

class Board extends Component {

    constructor(props) {
        super(props);
        this.state = { explanation: Object.keys(this.props.item),
            dificulty: Object.values(this.props.item),
            lstLength: Object.keys(this.props.item).length,
            posix: 0,
            loading: false,
            displayAvatar: false,
            language: this.props.language
        }
    }

    componentWillUpdate(nextProps) {
        // Any time props.item changes, update state.
        if (nextProps.language !== this.props.language){
            this.setState({
                language: nextProps.language
            })
        }else if (nextProps.item !== this.props.item) {
            this.setState({
                explanation: Object.keys(nextProps.item),
                dificulty: Object.values(nextProps.item),
                lstLength: Object.keys(nextProps.item).length,
                posix: 0,
                loading: false,
                displayAvatar: false
            })
            this.props.handleAvatar(false)

        }
    }

    handleNegativeFeedback = async () => {
        this.setState({
            loading:true
        })
        if(this.state.posix < this.state.lstLength-1){
            this.setState({
                posix: this.state.posix+1,
                loading: false
            })
        }else{
            const response = await Explanation.get('/summarization', {
                params: {
                    query: this.props.expression,
                    prev: this.state.explanation[this.state.posix]
                }
            })
            this.setState({
                explanation: Object.keys(response.data),
                dificulty: Object.values(response.data),
                lstLength: Object.keys(response.data).length,
                posix:0,
                loading: false
            })
        }
    };

    handleChangeAvatarValue = () => {
        this.setState({
            displayAvatar: !this.state.displayAvatar
        })
        this.props.handleAvatar(!this.state.displayAvatar)
    }

    render(){

        let lng = this.state.language

        function dif(value){
            if(value< 3){
                return "easy"
            }
            else if(value< 7){
                return "medium"
            }
            else{
                return "hard"
            }
        }

        const tooltipText = <span>
            Índice de legibilidade
            <p>1-3 Fácil</p>
            <p>3-7 Médio</p>
            <p>&gt;7 Dificil</p>
        </span>

            const feedback = <div id="feedback">
                <Button type="link"><LikeOutlined /></Button>
                <Popconfirm
                title={ i18n.t('display.board.feedback.tooltip.text', { lng }) }
                onConfirm={this.handleNegativeFeedback}
                onCancel={cancel}
                okText={ i18n.t('display.board.feedback.tooltip.positiveBtn', { lng }) }
                cancelText={ i18n.t('display.board.feedback.tooltip.negativeBtn', { lng }) }>
                <Button type="link"><DislikeOutlined /></Button>
            </Popconfirm>
        </div>

            var index = <div id="score"></div>
            if(this.state.language === "pt"){
                index = <div id="score"> Índice: &nbsp;
                <span difficulty={dif(this.state.dificulty[this.state.posix])}>{this.state.dificulty[this.state.posix]}</span> &nbsp;
                <Tooltip placement="bottomLeft" title={tooltipText}><InfoCircleOutlined /></Tooltip>
            </div>
            }


        return(
            <div id={this.props.index}>
                <Spin spinning={this.state.loading} size="large">
                    <Card title={`${this.props.index+1}. ${this.props.expression}`} style={{ width: '90%' }}>
                        <p>{this.state.explanation[this.state.posix]}  &nbsp; <a href={`https://www.google.com/search?q=${this.state.explanation[this.state.posix]}&tbm=isch`} target="_blank" rel="noopener noreferrer"><CameraOutlined style={{ fontSize: '30 px'}} /></a></p>
                        <p>
                            <Button type="primary" onClick={this.handleChangeAvatarValue}>{ i18n.t('display.board.button.display', { lng }) }<PlayCircleOutlined /></Button>
                            {index}
                            {feedback}
                        </p>
                    </Card>
                    <br />
                </Spin>
            </div>

        )
    }
}

export default Board;
