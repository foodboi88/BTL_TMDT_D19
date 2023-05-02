import React from "react";
import {
  Container,
  Divider,
  Dropdown,
  Grid,
  Header,
  Image,
  List,
  Menu,
  Segment
} from "semantic-ui-react";
import { Link, withRouter } from "react-router-dom";
import { connect } from "react-redux";
import { logout } from "../store/actions/auth";
import { fetchCart } from "../store/actions/cart";

class CustomLayout extends React.Component {
  componentDidMount() {
    this.props.fetchCart();
  }

  render() {
    const { authenticated, cart, loading } = this.props;
    return (
      <div>
        <Menu inverted>
          <Container>
            <Link to="/">
              <Menu.Item header>Trang chủ</Menu.Item>
            </Link>
            <Link to="/products">
              <Menu.Item header>Sản phẩm</Menu.Item>
            </Link>
            {/* <Link to="/statistic">
              <Menu.Item header>Thống kê</Menu.Item>
            </Link> */}
            {authenticated ? (
              <React.Fragment>
                <Menu.Menu position="right">
                  <Link to="/profile">
                    <Menu.Item>Trang cá nhân</Menu.Item>
                  </Link>
                  <Dropdown
                    icon="cart"
                    loading={loading}
                    text={`${cart !== null ? cart.order_items.length : 0}`}
                    pointing
                    className="link item"
                  >
                    <Dropdown.Menu>
                      {cart !== null ? (
                        <React.Fragment>
                          {cart.order_items.map(order_item => {
                            return (
                              <Dropdown.Item key={order_item.id}>
                                {order_item.quantity} x {order_item.item.title}
                              </Dropdown.Item>
                            );
                          })}
                          {cart.order_items.length < 1 ? (
                            <Dropdown.Item>Không có sản phẩm trong giỏ hàng</Dropdown.Item>
                          ) : null}
                          <Dropdown.Divider />

                          <Dropdown.Item
                            icon="arrow right"
                            text="Thanh toán"
                            onClick={() =>
                              this.props.history.push("/order-summary")
                            }
                          />
                        </React.Fragment>
                      ) : (
                        <Dropdown.Item>Không có sản phẩm trong giỏ hàng</Dropdown.Item>
                      )}
                    </Dropdown.Menu>
                  </Dropdown>
                  <Menu.Item header onClick={() => this.props.logout()}>
                    Đăng xuất
                  </Menu.Item>
                  <Link to="/statistic">
                    <Menu.Item header>Thống kê</Menu.Item>
                  </Link>
                </Menu.Menu>
              </React.Fragment>
            ) : (
              <Menu.Menu position="right">
                <Link to="/login">
                  <Menu.Item header>Đăng nhập</Menu.Item>
                </Link>
                <Link to="/signup">
                  <Menu.Item header>Đăng ký</Menu.Item>
                </Link>
              </Menu.Menu>
            )}
          </Container>
        </Menu>

        {this.props.children}

        <Segment
          inverted
          vertical
          style={{ margin: "5em 0em 0em", padding: "5em 0em" }}
        >
          <Container textAlign="center">
            <Grid divided inverted stackable>
              <Grid.Column width={3}>
                <Header inverted as="h4" content="GIÀY NIKE" />
                <List link inverted>
                  <List.Item as="a">Jordan 1</List.Item>
                  <List.Item as="a">Jordan 4</List.Item>
                  <List.Item as="a">Air force 1</List.Item>
                  <List.Item as="a">Nike blazer</List.Item>
                </List>
              </Grid.Column>
              <Grid.Column width={3}>
                <Header inverted as="h4" content="GIÀY KHÁC" />
                <List link inverted>
                  <List.Item as="a">New Balance</List.Item>
                  <List.Item as="a">MLB</List.Item>
                  <List.Item as="a">Alexander Mcqueen</List.Item>
                  <List.Item as="a">Dior</List.Item>
                </List>
              </Grid.Column>
              <Grid.Column width={3}>
                <Header inverted as="h4" content="Liên hệ với shop" />
                <List link inverted>
                  <List.Item as="a">Hướng dẫn đặt hàng</List.Item>
                  <List.Item as="a">Điều khoản và điều kiện thanh toán</List.Item>
                  <List.Item as="a">Chính sách giao hàng và nhận hàng</List.Item>
                  <List.Item as="a">Contact</List.Item>
                </List>
              </Grid.Column>
              <Grid.Column width={7}>
                <Header inverted as="h4" content="Shop Giày Điếu Cày" />
                <p>
                Tầng 4 - 161 Chùa Láng - Đống Đa - Hà Nội (Giờ Làm Việc từ 8am - 10pm)
                </p>
              </Grid.Column>
            </Grid>

            <Divider inverted section />
            <Image centered size="mini" src="/logo.png" />
            <List horizontal inverted divided link size="small">
              <List.Item as="a" href="#">
                Site Map
              </List.Item>
              <List.Item as="a" href="#">
                Contact Us
              </List.Item>
              <List.Item as="a" href="#">
                Terms and Conditions
              </List.Item>
              <List.Item as="a" href="#">
                Privacy Policy
              </List.Item>
            </List>
          </Container>
        </Segment>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    authenticated: state.auth.token !== null,
    cart: state.cart.shoppingCart,
    loading: state.cart.loading
  };
};

const mapDispatchToProps = dispatch => {
  return {
    logout: () => dispatch(logout()),
    fetchCart: () => dispatch(fetchCart())
  };
};

export default withRouter(
  connect(
    mapStateToProps,
    mapDispatchToProps
  )(CustomLayout)
);
