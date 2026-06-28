import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import { JwtPayload } from '../types/auth';
import { JwtRequest } from '../types/request';

export const authMiddleware = (req: Request, res: Response, next: NextFunction): void => {
  const authHeader = req.headers.authorization;

  // Authorization 헤더가 없거나 Bearer 형식이 아니면 거부한다
  if (!authHeader?.startsWith('Bearer ')) {
    res.status(401).json({ message: 'Unauthorized' });
    return;
  }

  // "Bearer <token>" 에서 토큰 부분만 추출한다
  const token = authHeader.split(' ')[1];

  try {
    // 검증 성공 시 페이로드를 JwtRequest의 jwtPayload에 주입한다
    // 이후 라우터 핸들러에서 (req as JwtRequest).jwtPayload로 접근한다
    (req as JwtRequest).jwtPayload = jwt.verify(token, process.env.JWT_SECRET!) as JwtPayload;
    next();
  } catch {
    // 만료, 서명 불일치 등 jwt.verify가 던지는 모든 에러를 동일하게 처리한다
    res.status(401).json({ message: 'Invalid token' });
  }
};
