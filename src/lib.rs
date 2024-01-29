wit_bindgen_rust::export!("add_one.wit");

struct AddOne;

impl add_one::AddOne for AddOne {
    fn add_one(n: i32) -> i32 {
        return n + 1;
    }
}

#[cfg(test)]
mod tests {
    use super::add_one::AddOne as _;
    use super::*;

    #[test]
    fn test_add_one() {
        assert_eq!(AddOne::add_one(1), 2);
        assert_eq!(AddOne::add_one(2), 3);
        assert_eq!(AddOne::add_one(3), 4);
    }
}