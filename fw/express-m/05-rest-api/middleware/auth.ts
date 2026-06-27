import { RequestHandler } from 'express';

export const auth: RequestHandler = (req, res, next) => {
  const token = req.headers['authorization'];
  if (!token) {
    res.status(401).json({ statusCode: 401, message: 'Unauthorized' });
    return;
  }
  // 실제 서비스에서는 JWT 검증 후 user 정보를 붙임
  req.user = { id: 1, name: '홍길동' };
  next();
};
